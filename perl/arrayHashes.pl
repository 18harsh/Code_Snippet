use strict;
use warnings;

use Data::Dumper;

$|=1;

sub main{

	my %hash1 =(
		"cats" => "milk",
		"dog" => "meat",
		"birds" => "seeds",
	);
	my @test;
	push @test, \%hash1;
	print $test[0]{"birds"}."\n";
}
main();