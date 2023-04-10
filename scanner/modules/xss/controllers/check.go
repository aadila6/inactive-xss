/*
 * @Author: liziwei01
 * @Date: 2023-03-30 12:07:14
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-04-10 18:39:26
 * @Description: file content
 */
/*
 * @Author: liziwei01
 * @Date: 2022-04-17 15:52:49
 * @LastEditors: liziwei01
 * @LastEditTime: 2022-04-17 15:57:14
 * @Description: file content
 */
package controllers

import (
	xssModel "github.com/liziwei01/gin-inactive-xss/modules/xss/model"
	xssService "github.com/liziwei01/gin-inactive-xss/modules/xss/services"
	"github.com/liziwei01/gin-lib/library/response"

	"github.com/gin-gonic/gin"
)

func Check(ctx *gin.Context) {
	inputs, hasError := getCheckPars(ctx)
	if hasError {
		response.StdInvalidParams(ctx)
		return
	}
	ret, err := xssService.Check(ctx, inputs)
	if err != nil {
		response.StdFailed(ctx, err.Error())
		return
	}
	response.StdSuccess(ctx, ret)
}

func getCheckPars(ctx *gin.Context) (xssModel.XSSPars, bool) {
	var inputs xssModel.XSSPars
	err := ctx.ShouldBind(&inputs)
	if err != nil {
		return inputs, true
	}
	return inputs, false
}
