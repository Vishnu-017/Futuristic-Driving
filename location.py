from geopy.geocoders import Nominatim
import time

def loc(place_name="Saralai"):
    """
    Get location details from a place name and return the city/town name.
    
    Args:
        place_name (str): Name of the place to geocode (default: "Saralai")
    
    Returns:
        str: City/town name extracted from the address, or None if failed
    """
    try:
        # Initialize Nominatim geocoder
        geolocator = Nominatim(user_agent="GetLoc")
        
        # Add small delay to respect API rate limits
        time.sleep(1)
        
        # Get location coordinates
        location = geolocator.geocode(place_name)
        if location is None:
            raise ValueError(f"Could not find location for {place_name}")
            
        latitude = location.latitude
        longitude = location.longitude
        
        print(f"Latitude = {latitude}")
        print(f"Longitude = {longitude}")
        
        # Reverse geocode to get full address
        reverse_location = geolocator.reverse(f"{latitude},{longitude}")
        if reverse_location is None:
            raise ValueError("Could not reverse geocode coordinates")
            
        address = reverse_location.address
        print(f"Full address: {address}")
        
        # Split address into components
        address_components = [comp.strip() for comp in address.split(',')]
        
        # Return the second component (typically city/town)
        if len(address_components) > 1:
            city = address_components[1]
            print(f"Extracted location: {city}")
            return city
        else:
            raise ValueError("Could not extract city from address")
            
    except Exception as e:
        print(f"Error in location processing: {str(e)}")
        return None

if __name__ == "__main__":
    # Test the function
    result = loc()
    if result:
        print(f"Final location result: {result}")
    else:
        print("Failed to determine location")
