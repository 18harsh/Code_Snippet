use strict;
use warnings;
use Data::Dumper;
use Getopt::Std;

$| = 1;
=pod 
	The is ACME XML parser version 1.0
	use with care
=cut	

sub main {
	my %opts;
	
	getopts('af:c', \%opts);
	# print Dumper(%opts);
	# my $file = $opts{'f'};
	# print "File: $file\n";
	if (!checkusage()){
		usage();
	}
}
sub checkusage{
	return 0;
}
sub usage{
	my $help = <<USAGE;

	hello
usage: perl GetCmdLine.pl-f <file name> -a
	-f <file name>:specify XML file name ro parse
	-a turn off error checking
example image:
perl GetCmdLine.pl -f test.xml -a

USAGE
	exit();
}
main();