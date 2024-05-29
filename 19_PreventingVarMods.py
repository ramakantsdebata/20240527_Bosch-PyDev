'''
How to prevent variable modification?

1. Using Immutables 
2. Encapsulating in classes
    Prefixing underscores '_' protected, '__' private
    Properties - 
        _age
        st1.age = 10 # <-- cannot be changed if setter not defined
        print(st1.age) # <-- Will work 
3. Using const
        MY_OUT = "console"
4. Freezing Objects
        frozenset()
5. Using third party libraries
        Modules like 'attr'
            @attr.s(frozen=True)
            my_const_data = 10
'''