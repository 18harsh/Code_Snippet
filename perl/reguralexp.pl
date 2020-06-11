use strict;
use warnings;

$|=1;
sub main(){
	my $file = 'requirements.txt';
	open(INPUT,$file) or die ("Input file $file not found\n");
	while(my $line = <INPUT>){
		if($line =~ /(t.....a.)(....)(.)/){
			print "$1$2$3\n";
		# The stuff matched by the first set of round brackets if now in $1
		# The stuff matched by the second set is in $2
		}
		# * matches zero or more of the preceding character; e.g.
		# d* matches zero or more d's 7* zero or more 7's, etc.
		# .* matches zero or more of any character, as many as possible
		# .*? matches zero or more of any character, as few as possible
		if($line =~ /(c.*?n)/){
			print "$1\n";
		}

	}
	close(INPUT);

}
main();
