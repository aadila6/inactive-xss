/*
 * @Author: liziwei01
 * @Date: 2023-04-10 18:41:07
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-04-10 19:36:56
 * @Description: file content
 */
package data

import (
	"context"
	"os"

	xssModel "github.com/liziwei01/gin-inactive-xss/modules/xss/model"
	"github.com/liziwei01/gin-lib/library/utils"
)

const (
	BaseDir  = "./temp_file/"
	FileName = "result.txt"
)

func Save(ctx context.Context, pars xssModel.XSSPars, ret string) error {
	var newFile *os.File
	var err error
	if !utils.File.IsExist(BaseDir) {
		err = utils.File.CreateDir(BaseDir)
		if err != nil {
			return err
		}
		newFile, err = os.Create(BaseDir + FileName)
		if err != nil {
			return err
		}
	} else {
		newFile, err = os.OpenFile(BaseDir + FileName, os.O_APPEND, 0666)
	}
	defer newFile.Close()
	_, err = newFile.WriteString(line(ctx, pars, ret))
	if err != nil {
		return err
	}
	return nil
}

func line(ctx context.Context, pars xssModel.XSSPars, ret string) string {
	return pars.Url + "\n" + ret + "\n\n"
}
