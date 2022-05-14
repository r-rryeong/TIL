- n진수 → 10진수: int(string, base)

  ```python
  print(int('111', 2))  #7
  print(int('222', 3))  #26
  print(int('333', 4))  #63
  print(int('FFF', 16))  #4095
  ```

- 10진수 → n진수

  ```python
  def convert(num, base):
      temp = '0123456789ABCDEF'
      q, r = divmod(num, base)
      
      if q == 0:
          return temp[r]
      else:
          return convert(q, base) + temp[r]
  ```

  

### 💡풀이

```python
def convert(num, base):
    temp = '0123456789ABCDEF'
    q, r = divmod(num, base)
    
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]
```

