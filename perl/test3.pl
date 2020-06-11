use strict;
use warnings;

use Data::Dumper;
$|=1;
sub main{
	my $input = "test.csv";

	open INPUT, $input or die "\nCan't open $input\n";
	<INPUT>;
	while(my $line =<INPUT>){
		chomp $line;
		$line=~ /\S+/ or next;
		$line=~ s/^\s*|s*$//g;
		my ($name, $payment,$date ) = split /\s*,\s*/, $line;
		

		print "$name : $payment :$date \n";

		#print $line."\n";
	}

	close INPUT
}
main();