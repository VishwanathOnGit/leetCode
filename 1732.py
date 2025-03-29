def largestAltitude(gain):
        current_altitude = 0
        max_altitude = 0
        
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude


# Example usage
gain = [-5,1,5,0,-7]
result = largestAltitude(gain)
print(result)  # Output: 1