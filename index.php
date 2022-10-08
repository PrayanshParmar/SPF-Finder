<?php
 
// Function to get the client IP address
function get_client_ip() {
    $ipaddress = '';
    if (isset($_SERVER['HTTP_CLIENT_IP']))
        $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
    else if(isset($_SERVER['HTTP_X_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_X_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED'];
    else if(isset($_SERVER['HTTP_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_FORWARDED'];
    else if(isset($_SERVER['REMOTE_ADDR']))
        $ipaddress = $_SERVER['REMOTE_ADDR'];
    else
        $ipaddress = 'UNKNOWN';
    return $ipaddress;
}
 
 
echo "Your IP address is: " . get_client_ip();














<!--<html> element is the root element of an HTML page -->
  <head><!--element contains meta information about the HTML page-->
    <title>PHP Test</title><!--element specifies a title for the HTML page (which is shown in the browser's title bar or in the page's tab) -->
  </head><!--head tag closing -->
  <body><!--element defines the document's body, and is a container for all the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.-->
    <?php echo '<p>Hello World</p>'; ?> <!--php print Hello World which is under paragraph tag -->

  </body><!--body tag closing -->
<!--</html>html tag closing -->