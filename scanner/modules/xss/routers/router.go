/*
 * @Author: liziwei01
 * @Date: 2022-04-18 17:27:34
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-04-08 09:37:22
 * @Description: file content
 */
package routers

import (
	xssControllers "github.com/liziwei01/gin-inactive-xss/modules/xss/controllers"

	"github.com/gin-gonic/gin"
)

/**
 * @description: 后台路由分发
 * @param {*}
 * @return {*}
 */
func Init(router *gin.RouterGroup) {
	userGroup := router.Group("/xss")
	{
		userGroup.POST("/check", xssControllers.Check)
	}
}
