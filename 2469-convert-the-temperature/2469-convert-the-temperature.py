class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        #formula for celsius to kelvin and kelvin to celsius
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        
        return [kelvin,fahrenheit]
        