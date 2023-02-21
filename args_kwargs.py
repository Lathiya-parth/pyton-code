def fun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
fun(first_name='parth',last_name='lathiya')
d={'name':'parth','age':19}
fun(**d)