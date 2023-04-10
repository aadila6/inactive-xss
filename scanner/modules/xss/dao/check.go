/*
 * @Author: liziwei01
 * @Date: 2023-03-30 12:07:14
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-04-08 11:19:17
 * @Description: file content
 */
package dao

import (
	"context"

	xssModel "github.com/liziwei01/gin-inactive-xss/modules/xss/model"
)

func Register(ctx context.Context, pars xssModel.XSSPars) error {
	// client, err := mysql.GetClient(ctx, constant.SERVICE_CONF_DB_IDIARY_USER)
	// if err != nil {
	// 	return err
	// }

	// tableName := USER_PRIVATE_INFO_TABLE

	// mapSliceInsertData := []map[string]interface{}{}
	// mapSliceInsertData = append(mapSliceInsertData, map[string]interface{}{
	// 	"email":    pars.Email,
	// 	"password": pars.Password,
	// 	"nickname": pars.Username,
	// })

	// _, err = client.Insert(ctx, tableName, mapSliceInsertData)
	// if err != nil {
	// 	return err
	// }

	return nil
}
