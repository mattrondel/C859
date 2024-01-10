https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/cannot-install-snmp-wmisnmpprovider


# Define switch details
$switchIpAddress = "your_switch_ip_address"
$snmpCommunityString = "your_snmp_community_string"

# Define laptop MAC address
$laptopMacAddress = "xx-xx-xx-xx-xx-xx"

# SNMP OID for ifPhysAddress (MAC address) table
$oidIfPhysAddress = "1.3.6.1.2.1.2.2.1.6"

# Construct SNMP request command
$snmpCommand = "snmpwalk -v 2c -c $snmpCommunityString $switchIpAddress $oidIfPhysAddress"

# Execute SNMP request
$result = Invoke-Expression -Command $snmpCommand

# Check if laptop MAC address is found in the SNMP results
if ($result -match $laptopMacAddress) {
    Write-Host "Laptop is connected to the switch."
} else {
    Write-Host "Laptop is not connected to the switch."
}

#Replace the placeholders (your_switch_ip_address, your_snmp_community_string, and xx-xx-xx-xx-xx-xx) with your actual switch IP address, SNMP community string, and the MAC address of the laptop you want to check.

#Note: SNMP community strings are essentially passwords, and it's crucial to ensure they are secure. Additionally, SNMP needs to be enabled and properly configured on the Cisco switch for this script to work.

#This script uses the SNMP protocol to retrieve the MAC addresses associated with each switch port. It then checks if the specified laptop MAC address is present in the results, indicating that the laptop is connected to the switch. Keep in mind that the specific SNMP OIDs might vary depending on the Cisco switch model and firmware version. You may need to adjust the script accordingly based on your switch's SNMP MIB structure.

# To be notified when a laptop becomes disconnected from the network using SNMP and PowerShell, you can set up a script that regularly checks the status of the laptop's MAC address on the switch using SNMP. If the script detects that the MAC address is no longer associated with any port on the switch, it can trigger a notification.

# Define switch details
$switchIpAddress = "your_switch_ip_address"
$snmpCommunityString = "your_snmp_community_string"

# Define laptop MAC address
$laptopMacAddress = "xx-xx-xx-xx-xx-xx"

# SNMP OID for ifPhysAddress (MAC address) table
$oidIfPhysAddress = "1.3.6.1.2.1.2.2.1.6"

# Function to check if laptop MAC address is present in SNMP results
function CheckLaptopStatus {
    $snmpCommand = "snmpwalk -v 2c -c $snmpCommunityString $switchIpAddress $oidIfPhysAddress"
    $result = Invoke-Expression -Command $snmpCommand

    if ($result -match $laptopMacAddress) {
        return $true  # Laptop is connected
    } else {
        return $false  # Laptop is not connected
    }
}

# Function to send a notification
function SendNotification {
    # Replace this with your preferred notification mechanism (e.g., sending an email, using a messaging service, etc.)
    Write-Host "Laptop is disconnected from the network. Send notification here."
}

# Check laptop status and send notification if disconnected
if (-not (CheckLaptopStatus)) {
    SendNotification
}

# Remember to replace the placeholders (your_switch_ip_address, your_snmp_community_string, and xx-xx-xx-xx-xx-xx) with your actual switch IP address, SNMP community string, and the MAC address of the laptop you want to monitor.

# You can schedule this script to run periodically using a task scheduler like Task Scheduler in Windows. If the script detects that the laptop is disconnected, it will trigger the notification function.

# Note: SNMP is not always instant in reflecting changes, and the detection might have a delay. 

