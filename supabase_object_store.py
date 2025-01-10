from supabase import create_client, Client

SUPABASE_URL = "https://enhqxzbqlrzpgshfsivl.supabase.co" # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVuaHF4emJxbHJ6cGdzaGZzaXZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY1MDE3MzUsImV4cCI6MjA1MjA3NzczNX0.6NMPpFCMmKNmazJ_WBOLAbWML6mW_Xne-nI3zMX2cfI" # Replace with your Supabase API key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Step 1: Create a storage bucket
#bucket_name = "imgs2" # Name of the bucket to be created
#try:
 #   response = supabase.storage.create_bucket(bucket_name,   
  #  options={
   #     "public": True, # Make the bucket public
    #    "allowed_mime_types": ["image/png"], # Allow only PNG images
     #   "file_size_limit": 1024*1024, # Limit file size to 1MB
    #}
    #)
    #print(f"Bucket '{bucket_name}' created successfully.")
#except Exception as e:
 #   print(f"Bucket creation error: {e}")

# # Step 2: Upload an image to the bucket
image_path = "D:\supa\cat.jpeg.jpg"  # Replace with the local image path
image_name = "cat.jpeg"  # Desired name for the uploaded file

try:
     with open(image_path, 'rb') as f:
         response = supabase.storage.from_("imgs2").upload(
             file=f, # File object
             path=image_name,  # Name of the file in the bucket
             file_options={"content-type":"image/png","cache-control": "3600", "upsert": False}, 
         )
         print(f"Image uploaded successfully: {response}")
except Exception as e:
     print(f"Image upload error: {e}")


# # Step 3: Get the public URL of the image
try:
     public_url =  supabase.storage.from_("imgs2").get_public_url(
   "iD:\supa\cat.jpeg.jpg"
 )
     print(f"Public URL of the image: {public_url}")
except Exception as e:
     print(f"Error getting public URL: {e}")

