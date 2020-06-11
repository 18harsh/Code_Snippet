use strict;
use warnings;

$|=1;

sub main{

	my @files = (
		'logo.jpg',
		'home.html',
		'tutorial4.pl',
		'no_file.txt',
		);
	foreach my $file(@files){
		print "$file\n";
		if (-f $file)	{
			print "Found file: $file\n\n";
		}
		else{
			print "File Not Found\n\n";
		}
	}

}
main();
