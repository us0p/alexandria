class Variables {
    // Note that class fields doesn't need to be initialized, in those 
    // cases they'll be initialized to their default values as stated 
    // below.
    // Note however that this is considered bad programming style.
    
    // instace variable 
    // primitive types {
        // 32-bit signed two's complement integer.
	// since Java SE 8, you can use this type to represent unsigned 
	// 32-bit integer.
	// default values = 0
        int number = 0;
	int hex = 0x1a;
	int bin = 0b11010;
	int big = 1_000_000;
        
        // 8-bit signed two's complement integer.
	// default values = 0
        byte b = 0;
    
        // 16-bit signed two's complement integer
	// default values = 0
        short s = 0;
    
        // 64-bit two's complement integer.
	// since Java SE 8, you can use this type to represent unsigned 
	// 64-bit long numbers.
	// default values = 0L
        long l = 0L;
    
        // single-precision 32-bit IEEE 754 floating point.
	// default values = 0.0f
        float f = 0.0f;
    
        // double-precision 64-bit IEEE 753 floating point.
        // for decimal values, this data type is generally the default 
	// choice and because of that, the trailing d can be ommited.
	// default values = 0.0d
        double d = 0.0;
    
        // only two possible values: true or false.
	// default values = false
        boolean bool = false;
    
        // single 16-bit Unicode character.
	// always use single quotes for char literals and double quotes for
	// String literals.
	// default values = \u0000
        char c = 'a';

	// String (or any object)
	// default value = null
	
	// class literal, formed by taking a type name and appending 
	// .class. It refers to the object that represents the type itself 
	// of type Class;
	Class cls = String.class;
    //}

    // class variable
    static int anotherNumber = 0;
    
    // read only
    final int yetAnotherNumber = 0;

    // parameters are always classified as variables.
    void localVariable() {
	// The compiler never assigns a default value to an unintialized 
	// local variable.
	int variable = 0;
    }
}
