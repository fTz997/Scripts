#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(int argc, char *argv[]){
	int mySocket;
	int connection;
	int port;
	int start = 0;
	int finish = 65535;
	char *destination;
	destination = argv [1];

	struct sockaddr_in target;

	for (port = start; port < finish, port++ ){
		mySocket = socket(AF_INET, SOCK_STREAM,0);
		target.sin_family = AF_INET;
		target.sin_port = htons(port);
		target.sin_addr.s_addr = inet_addr(destination);

		connection = connect(mySocket, (struct sockaddr *) &target, sizeof target);

		if(connect == 0){
			printf("Porta %d - status [ABERTA] \n");
			close(mySocket);
			close(connection);
		} else {
			pclose(mySocket);
			close(connection);
		}
	}
}
