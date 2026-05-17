class Solution {
    public int[] fun1(int[] arr){
        Stack<Integer> s1=new Stack<>();
        int[] arr1=new int[arr.length];
        for(int i=arr.length-1;i>=0;i--){
        while(!s1.isEmpty() && arr[s1.peek()]>=arr[i]){
            s1.pop();
        }
        if(s1.isEmpty()){
            arr1[i]=arr.length;
        }
        else{
            arr1[i]=s1.peek();
        }
        s1.push(i);
        }
        return arr1;
    }
    public int[] fun2(int[] arr){
        Stack<Integer> s2=new Stack<>();
        int[] arr2=new int[arr.length];
        for(int i=0;i<arr.length;i++){
        while(!s2.isEmpty() && arr[s2.peek()]>arr[i]){
            s2.pop();
        }
        if(s2.isEmpty()){
            arr2[i]=-1;
        }
        else{
            arr2[i]=s2.peek();
        }
        s2.push(i);
        }
        return arr2;
    }
    public int sumSubarrayMins(int[] arr) {
        
        int []arr1=fun1(arr);
        int []arr2=fun2(arr);
        int mod=(int)1e9+7;
       long total = 0;

for (int i = 0; i < arr.length; i++) {
    long left = i - arr2[i];
    long right = arr1[i] - i;

    total = (total + (arr[i] * left * right) % mod) % mod;
}

return (int) total;

    }
}