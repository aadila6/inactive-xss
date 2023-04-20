/*
 * @Author: liziwei01
 * @Date: 2022-04-18 17:27:34
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-04-11 15:10:05
 * @Description: file content
 */
package data

import (
	"context"
	"strings"

	xssModel "github.com/liziwei01/gin-inactive-xss/modules/xss/model"
)

func Check(ctx context.Context, pars xssModel.XSSPars) (bool, error) {
	ret := false
	gadgets := []string{"jquery"}
	for i := 0; i != len(gadgets); i++ {
		if strings.Contains(pars.Snippet, gadgets[i]) {
			ret = true
			Save(ctx, pars, gadgets[i])
		}
	}
	return ret, nil
}
