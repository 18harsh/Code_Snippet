use strict;
use warnings;
$|=1;#output buffering
sub main(){
	my $text = "The code for this device is GP8765.";
	if ($text =~/(\w\w\d{2,6})/){
		print "The code is $1";		
	}
	else{
		print "Not Found";
	}
}

main();