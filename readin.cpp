#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using  namespace std;
void readin()
{
	freopen("hosts.txt","r",stdin);
	int seq;
	string ip,username,passwd,info;
	while(cin>>seq>>ip>>username>>passwd>>info)
	{
		cout<<seq<<"+"<<ip<<"+"<<username<<"+"<<passwd<<"+"<<info<<endl;
	}
}
int main()
{
	readin();
	return 0;
}
