use strict;
use warnings;
$|=1;#output buffering
sub main(){
	my @emails = (
		'john@capeofprogramming.com',
		'hello',
		'@llkj.com',
		'njn546@somewhre77.com',
		'kh@2344.',);
	for my $email(@emails){
		if ($email =~/\w+\@\w+\.\w+/){

			print ("valid email:$email\n");
		}
	} 
}

main();