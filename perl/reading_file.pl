use strict;
use warnings;

$|=1;
sub main(){
	my $file = 'requirements.txt';

	open(INPUT,$file) or die ("Input file $file not found\n");

	while(my $line = <INPUT>){
		if($line =~ /Markup/){
			print $line;
		}

	}

	close(INPUT);
}
main();