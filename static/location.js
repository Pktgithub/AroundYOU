function getLocation(type) {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        document.getElementById("latitude").value = position.coords.latitude;
        document.getElementById("longitude").value = position.coords.longitude;
        document.getElementById("place_type").value = type; 
        document.getElementById("locationForm").submit(); // submit to backend
      },
      (error) => {
        alert("Unable to retrieve location.");
        console.error(error);
      }
    );
  } else {
    alert("Geolocation is not supported by your browser.");
  }
}
