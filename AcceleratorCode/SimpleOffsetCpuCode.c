/**
* Document: Homogeniety Edge Detection on greyscale pixels
* Written by William Huibregtse
* Based on Maxeler SimpleOffset template on simulator
 */

#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <MaxSLiCInterface.h>
#include "Maxfiles.h"

int check(int n, uint8_t *dataOut, uint8_t *expected, int row_width)
{
	int status = 0;

    // Print all elements block
    printf("Output Matrix:\n");
	for (int i = 0; i < n; i++) // First and last data point are undefined!
	{
		printf("%d, ", dataOut[i]);
		if (i % row_width == row_width - 1){
		    printf(" \n");
		}
	}
	
	printf("Expected Matrix:\n");
	for (int i = 0; i < n; i++) // First and last data point are undefined!
	{
		printf("%d, ", expected[i]);
		if (i % row_width == row_width - 1){
		    printf(" \n");
		}
	}
	return status;
}

int main()
{
	const int N = 16;
	size_t sizeBytes = N * sizeof(uint8_t);
	uint8_t dataIn[] = {112, 12, 35, 61,
                        0, 155, 21, 2,
                        55, 156, 94, 90,
                        87, 2, 37, 96};
	uint8_t *dataOut = malloc(sizeBytes);
	uint8_t expected[] = {112, 143, 120, 59,
                          156, 155, 135, 92,
                          101, 156, 92, 88,
                          85, 154, 119, 59};

	printf("Running DFE.\n");
	SimpleOffset(N, dataIn, dataOut);
	int status = check(N, dataOut, expected, 4);
	if (status)
		printf("Test failed.\n");
	else
		printf("Test passed OK!\n");
	return status;
}
