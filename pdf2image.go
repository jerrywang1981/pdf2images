package main

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/jerrywang1981/handy-tools/pdf"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Please call in format: ./pdf2image input_folder output_folder")
		return
	}
	inputFolder, outputFolder := os.Args[1], os.Args[2]
	input, err := filepath.Abs(inputFolder)
	if err != nil {
		fmt.Println(err)
		return
	}
	fileInfo, err := os.Stat(input)
	if os.IsNotExist(err) {
		fmt.Println(err)
		return
	}
	if !fileInfo.IsDir() {
		fmt.Println("it is not folder")
		return
	}

	output, err := filepath.Abs(outputFolder)
	if err != nil {
		fmt.Println(err)
		return
	}
	fileInfo, err = os.Stat(output)
	if os.IsNotExist(err) {
		fmt.Println(err)
		return
	}
	if !fileInfo.IsDir() {
		fmt.Println("it is not folder")
		return
	}

	err = pdf.ConvertPdfToImage(input, output)
	if err != nil {
		fmt.Println(err)
		return
	}

}
