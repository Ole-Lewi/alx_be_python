def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unexpected errors
        return f"Unexpected error: {str(e)}"
