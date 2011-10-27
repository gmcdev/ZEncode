import pexpect

child = pexpect.spawn( 'ssh nitram@ftp.modwest.com' )
child.expect( 'password:' )
child.sendline( 'b33rgen0' )
child.expect( 'nitram@shell1:\/\$' )
child.sendline( 'ls -l' )
print child
