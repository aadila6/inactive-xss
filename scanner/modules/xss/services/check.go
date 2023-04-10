/*
 * @Author: liziwei01
 * @Date: 2022-04-12 14:24:06
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-04-10 19:16:21
 * @Description: file content
 */
package services

import (
	"context"

	xssData "github.com/liziwei01/gin-inactive-xss/modules/xss/data"

	xssModel "github.com/liziwei01/gin-inactive-xss/modules/xss/model"
)

func Check(ctx context.Context, pars xssModel.XSSPars) (bool, error) {
	// do the check
	result, err := xssData.Check(ctx, pars)
	if err != nil {
		return false, err
	}
	return result, err
}
