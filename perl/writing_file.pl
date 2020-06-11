use strict;
use warnings;

$|=1;
sub main(){

	my $file = 'requirements.txt';
	open(INPUT,$file) or die ("Input file $file not found\n");

	my $output = "output.txt";
	open(OUTPUT,'>'.$output) or die("Can't create $output.");

	while(my $line = <INPUT>){

		;
		if($line =~ /l.t/){
			$line =~ s/the/THE/ig;
			print OUTPUT $line;
			print $line;
		}

	}

	close(INPUT);
	close(OUTPUT);

}
main();