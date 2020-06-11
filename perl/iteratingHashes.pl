use strict;
use warnings;

use Data::Dumper;

$|=1;

sub main{
	my %food = (
		"cats" => "milk",
		"dog" => "meat",
		"birds" => "seeds",
	);

	my ($one, $two, $three) = (1,2,3);

	print "The value of \$two is $two\n";

	while(my ($key,$value) =each %food){
		print "$key:$value\n"
	}
	
	foreach my $key(sort keys %food){
		my $values = $food{$key};
		print "$key = $values\n";
	}
}
main();