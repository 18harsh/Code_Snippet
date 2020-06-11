use strict;
use warnings;

use LWP::Simple;

$|=1;
sub main {
	my $content = get("https://www.flipkart.com/hp-x3500-wireless-comfort-mouse/p/itmewwdecwfdzkys?pid=ACCDTR26FPQK7T9F&marketplace=FLIPKART");

	unless(defined($content)){
		die "Unreachable url\n";
	}

	# while($content =~ m|<\s*a\s+[^>]*href\s*=\s*['"]([^>"']+)['"][^>]*>([^<>]*)</|sig){
	# 	print "$2: $1\n";
	# }
	while($content =~ m|(6\d\d)(6\d\d.?)|sig){	
		if( $1 == 699){
			print " $1 ; $2\n";
		}
	}

		
}
main();