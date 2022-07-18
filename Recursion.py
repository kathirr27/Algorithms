#### This code will tell you how to do recursion #####

def do_fibo(n):
  """
  This procedure will call recursivley for calculating Nth fibnacci series 
  """ 
    if n == 2:
        return 1
    if n == 1:
        return 0

    return do_fibo(n-1)+ do_fibo(n-2)
  

print(do_fibo(5))
