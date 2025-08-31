Import-Module WebAdministration
$ErrorActionPreference = 'SilentlyContinue'

Get-Website | ForEach-Object {
    $site = $_

    # Collect configuration read errors per site without terminating
    $configErrors = New-Object System.Collections.Generic.List[string]

    # Bindings usually safe; still guard just in case
    $bindings = @()
    try {
        $bindings = $site.Bindings.Collection | ForEach-Object {
            @{ Protocol = $_.protocol; BindingInformation = $_.bindingInformation }
        }
    } catch {
        $configErrors.Add("Bindings: $($_.Exception.Message)") | Out-Null
        $bindings = @()
    }

    # Authentication settings (may fail if web.config is malformed)
    $authAnon = $null
    $authWin  = $null
    try {
        $authAnon = (Get-WebConfigurationProperty -Filter "system.webServer/security/authentication/anonymousAuthentication" -PSPath "IIS:\Sites\$($site.Name)" -Name enabled -ErrorAction Stop).Value
    } catch {
        $configErrors.Add("Authentication(Anonymous): $($_.Exception.Message)") | Out-Null
    }
    try {
        $authWin = (Get-WebConfigurationProperty -Filter "system.webServer/security/authentication/windowsAuthentication" -PSPath "IIS:\Sites\$($site.Name)" -Name enabled -ErrorAction Stop).Value
    } catch {
        $configErrors.Add("Authentication(Windows): $($_.Exception.Message)") | Out-Null
    }
    $authSettings = @{ Anonymous = $authAnon; Windows = $authWin }

    # HSTS block (property exists on newer IIS only)
    $hsts = $null
    try {
        if ($site.PSObject.Properties.Name -contains "Hsts") {
            $hsts = @{
                Enabled              = $site.Hsts.Enabled
                IncludeSubDomains    = $site.Hsts.IncludeSubDomains
                MaxAge               = $site.Hsts.MaxAge
                Preload              = $site.Hsts.Preload
                RedirectHttpToHttps  = $site.Hsts.RedirectHttpToHttps
            }
        }
    } catch {
        $configErrors.Add("HSTS: $($_.Exception.Message)") | Out-Null
        $hsts = $null
    }

    # Advanced properties that query configuration
    $customErrorMode = $null
    $defaultDocs = @()
    try {
        $customErrorMode = (Get-WebConfigurationProperty -Filter "system.webServer/httpErrors" -PSPath "IIS:\Sites\$($site.Name)" -Name "errorMode" -ErrorAction Stop).Value
    } catch {
        $configErrors.Add("HttpErrors: $($_.Exception.Message)") | Out-Null
    }
    try {
        $defaultDocs = (Get-WebConfigurationProperty -Filter "system.webServer/defaultDocument/files" -PSPath "IIS:\Sites\$($site.Name)" -Name "value" -ErrorAction Stop) | ForEach-Object { $_.Value }
    } catch {
        $configErrors.Add("DefaultDocument: $($_.Exception.Message)") | Out-Null
        $defaultDocs = @()
    }

    # Compose output with non-terminating error details
    [PSCustomObject]@{
        Name              = $site.Name
        Id                = $site.Id
        State             = $site.State
        PhysicalPath      = $site.PhysicalPath
        ApplicationPool   = $site.applicationPool
        Bindings          = $bindings
        AutoStart         = $site.ServerAutoStart
        WebConfigIssue    = ($configErrors.Count -gt 0)
        WebConfigError    = if ($configErrors.Count -gt 0) { $configErrors -join "; " } else { $null }
        # --- ADVANCED ---
        Advanced = @{
            Description             = $site.Description
            LogFileDirectory        = $site.logFile.directory
            LogFormat               = $site.logFile.logFormat
            LogPeriod               = $site.logFile.period
            LogTruncationSizeBytes  = $site.logFile.truncateSize
            Limits = @{
                ConnectionTimeoutSeconds      = $site.limits.connectionTimeout.TotalSeconds
                MaximumBandwidthBytesPerSec   = $site.limits.maxBandwidth
                MaximumConnections            = $site.limits.maxConnections
                MaximumUrlSegments            = $site.limits.maxUrlSegments
            }
            PreloadEnabled              = $site.preloadEnabled
            EnabledProtocols            = $site.enabledProtocols
            ServiceAutoStartProviders   = $site.ServiceAutoStartProviders
            TraceEnabled                = $site.TraceFailedRequestsLogging.Enabled
            CustomErrorPages            = $customErrorMode
            DefaultDocument             = $defaultDocs
            Authentication              = $authSettings
            HSTS                        = $hsts
            WebConfigStatus             = if ($configErrors.Count -gt 0) { "Partial (site configuration could not be fully read)" } else { "OK" }
            WebConfigErrors             = if ($configErrors.Count -gt 0) { $configErrors } else { $null }
        }
    }
} | ConvertTo-Json -Depth 6
