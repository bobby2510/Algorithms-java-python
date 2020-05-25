//Knath morris pratt(KMP) algorithm
//Time complexity O(n+m)
/*
	author: bobby2510
	date_coded: 25/05/2020
 */
/*
	Ip:
	ababcabcabababd
	ababd
	Op:
	10
 */
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
public class Kmp {
public static void main(String []args) throws IOException
{
	InputStreamReader isr=new InputStreamReader(System.in);
	BufferedReader br=new BufferedReader(isr);
	String s=br.readLine().trim();
	String p=br.readLine().trim();
	int ans=go(s,p);
	if(ans<0) System.out.println("Pattern not found!");
	else System.out.println("Found at : "+ans);
}
// actual kmp algorithm 
public static int go(String s,String p)
{
	int n=s.length(),m=p.length(),ans=-1,i=0,j=0;
	int []lpa=get_go_lpa(p,m);
	while(i<n)
	{
		if(s.charAt(i)==p.charAt(j))
		{
			i++;
			j++;
		}
		else
		{
			while(true)
			{
				j=lpa[j];
				if(s.charAt(i)==p.charAt(j))
				{
					i++;
					j++;
					break;
				}
				if(j==0)
				{
					i++;
					break;
				}
			}
			
		}
		if(j==m)
		{
			ans=i-m;
			break;
		}
	}
	return ans;
}
// longest prefix and suffix array
public static int[] get_go_lpa(String p,int m)
{
	int []lpa=new int[m+1];
	int curr_index=0,curr_count=0;
	for(int i=2;i<=m;i++)
	{
		if(p.charAt(curr_index)==p.charAt(i-1))
		{
			curr_count++;
			curr_index++;
		}
		else 
		{
			curr_count=0;
			curr_index=0;
		}
		lpa[i]=curr_count;
	}
	return lpa;
}
}
