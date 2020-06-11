use strict;
use warnings;
use LWP::Simple;
sub main {
	print "Downloading....\n";
	#print get("http://mu.ac.in/");
#	getstore("http://mu.ac.in/","home.html");
	my $code = getstore('http://mu.ac.in/virtual-tour/',"logo.jpg");
	if ($code == 200){
		print "success\n"
	}
	else{
		print "Failed\n"
	}
	print "Finished\n";	
}
main();