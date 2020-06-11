use strict;
use warnings;

use Data::Dumper;
$|=1;

sub main{
	my %months = (
		"jan" =>1,
		"feb" =>2,
		"march" =>3,
		"april" =>4,
		"june" =>6,
		);
	print $months{"jan"} ."\n";

	while(my ($key,$value) =each %months){
		print "$key:$value\n"
	}

	my @months = keys %months;

	foreach my $month(@months){
		my $value = $months{$month};
		print "$month : $value\n";
	}

}
main();