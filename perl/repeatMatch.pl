use strict;
use warnings;

use LWP::Simple;

$|=1;
sub main{
	my $content = get("https://www.flipkart.com/hp-x3500-wireless-comfort-mouse/p/itmewwdecwfdzkys?pid=ACCDTR26FPQK7T9F&marketplace=FLIPKART");

	unless(defined($content)){
		die "Unreachable url\n";
	}

	my @ classes = $content=~ m|class="([^"'']*?)"|ig;

	if (@classes == 0){
		print "No Matches";
	}
	else{
		foreach my $class(@classes){
			print "$class\n";	
		}
	}
	
	
}
main();