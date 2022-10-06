def dbl_linear(n)
  # your code
  count = 0
  u = [1]
  while u.size <= n*2
    u << 2*u[count] +1
    u << 3*u[count] +1
    u.sort!.uniq!
    count += 1
  end
  return u[n]
end

#can't reach the time limit
# can't achieve to get a more efficient code
