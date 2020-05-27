// Rabin Karps Algorithm
// time complexity O(n) 
/*
	author: bobby2510
	date_coded: 26/05/2020
*/
/*
	Ip:
	fakdfjakdsfjakfjadfkldafmdakfjdakfjaksfjadkfjalkdfjakl
	jaksfjadkf
	Op:
	Found at : 34
 */
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
public class Rabin_Karp_Algo {
public static long mod=1000000007;
public static void main(String []args) throws IOException
{
	InputStreamReader isr=new InputStreamReader(System.in);
	BufferedReader br=new BufferedReader(isr);
	String s=br.readLine().trim(),p=br.readLine().trim();
	int ans=go(s,p);
	if(ans<0) System.out.println("Pattern not found!");
	else System.out.println("Found at : "+ans);
}
public static int go(String s,String p)
{
	int n=s.length(),m=p.length(),ans=-1;
	long []mem=go_get_mem(n);
	long []hash=go_get_hash(mem,s,n);
	long req_hash=0;
	for(int i=0;i<m;i++) 
		req_hash=(req_hash%mod+((long)p.charAt(i)*mem[i])%mod)%mod;
	if(req_hash==hash[m-1]) return 0;
	for(int i=1;i<n-m+1;i++)
	{
		long curr_hash=(hash[i+m-1]+mod-hash[i-1])%mod;
		if(curr_hash==(req_hash*mem[i])%mod)
		{
			if(s.substring(i,i+m).equals(p))
			{
				ans=i;
				break;
			}
		}
	}
	return ans;
}
public static long[] go_get_mem(int n)
{
	long []mem=new long[n+1];
	mem[0]=1;
	for(int i=1;i<=n;i++)
		mem[i]=(mem[i-1]*31)%mod;
	return mem;
}
public static long[] go_get_hash(long[] mem,String s,int n)
{
	long []hash=new long[n];
	hash[0]=(long)s.charAt(0);
	for(int i=1;i<n;i++)
		hash[i]=(hash[i-1]%mod+((long)s.charAt(i)*mem[i])%mod)%mod;
	return hash;
}
}
