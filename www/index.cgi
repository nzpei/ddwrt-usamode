#!/jffs/usa/haserl
Content-Type: text/html
Cache-Control: no-cache
Expires: Tue, 01 Jan 1980 00:00:00 GMT

<?
# Current VPN Gateway Address (required for route)
VPNGW=`/sbin/route -n | grep tun0 | grep UGH | awk '{print $2}'`

# Get the current USAMODE state of the user
/usr/sbin/ip rule list | grep "lookup 200" | grep $REMOTE_ADDR >/dev/null 2>&1
if [ $? -eq 0 ]; then
   USAMODE="ON"
else
   USAMODE="OFF"
fi

# If Form was submitted, action a toggle.
if [ "$FORM_toggle" == "Y" ]; then
   # Logic to toggle USA Mode
   if [ "$USAMODE" == "ON" ]; then
      # Remove the rule 
      /usr/sbin/ip rule del from $REMOTE_ADDR table 200
      /usr/sbin/ip route flush cache
   else
      # If route for table 200 doesn't exist, add it
      /usr/sbin/ip route show table 200 | grep $VPNGW >/dev/null 2>&1
      if [ $? -ne 0 ]; then
         /usr/sbin/ip route add default via $VPNGW dev tun0 table 200 
      fi 
      # Turn on USA mode for this device
      /usr/sbin/ip rule add from $REMOTE_ADDR table 200
      /usr/sbin/ip route flush cache
   fi
fi

# Refresh the current USAMODE state of the user
/usr/sbin/ip rule list | grep "lookup 200" | grep $REMOTE_ADDR >/dev/null 2>&1
if [ $? -eq 0 ]; then
   USAMODE="ON"
else
   USAMODE="OFF"
fi
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>Toggle USA Mode</title> 
</head>
<body>

<h1>Toggle USA Mode</h1>
<p>Your current IP address is: <?
echo $REMOTE_ADDR
?>
</p>
<p>The current OpenVPN Gateway is: <?
echo $VPNGW
?>
</p>

<p>USA Mode for your device is currently <?
echo $USAMODE

?>
</p>
<form id="toggleform" method="post" action="index.cgi">
<input name="toggle" type="hidden" value="Y">
<input name="Submit1" type="submit" value="Toggle">
</form>

</body>
</html>
