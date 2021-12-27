#include <stdio.h>
#include <iostream>
#include <curl/curl.h>

//g++ helloworld.cpp -lcurl -o hello



// write data use by curl
size_t write_data(void *ptr, size_t size, size_t nmemb, FILE *stream)
{
  size_t	written;
  
  written = fwrite(ptr, size, nmemb, stream);
  return written;
}


int main(void)
{
  CURL *curl;
  CURLcode result;
  FILE *ftpFile;
  std::string	file1 = "";
  std::string	file2 = "";

  ftpFile = fopen("tmpFile.pdf", "wb");


  curl_global_init(CURL_GLOBAL_DEFAULT);

  curl = curl_easy_init();
  if (curl) {

    // Set URL
    curl_easy_setopt(curl, CURLOPT_URL, "http://index-of.co.uk/Programming/Perl%20como%20herramienta%20de%20administracion.pdf");
    // curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, ftpFile);

    // If you want to set any more options, do it here, before making the request.

    // Perform the request which prints to stdout
    result = curl_easy_perform(curl);

    // Error check
    if (result != CURLE_OK) {
      std::cerr << "Error during curl request: " 
                << curl_easy_strerror(result) << std::endl;
    }

    curl_easy_cleanup(curl);
  } else {
    std::cerr << "Error initializing curl." << std::endl;
  }

  fclose(ftpFile);
  curl_global_cleanup();

  return 0;
}
