#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
using namespace std;

int main()
{
	//getName(sftppath);
    FILE* fp=fopen("testdir/log.txt","w");
    fprintf(fp,"%s","mem");
    fclose(fp);
	//cout<<ret<<"---"<<res<<endl;
	return 0;
}