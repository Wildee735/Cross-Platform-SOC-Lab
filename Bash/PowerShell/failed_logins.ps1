Get-WinEvent -FilterHashtable @{
    LogName='Security'
    Id=4625
} |
Select-Object TimeCreated, Message |
Export-Csv FailedLogins.csv -NoTypeInformation
