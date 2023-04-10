/*
 * @Author: liziwei01
 * @Date: 2023-03-30 12:07:14
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-04-10 18:37:29
 * @Description: file content
 */
package model

type XSSPars struct {
	Url string `form:"url" json:"url" binding:"required"`
	Snippet string `form:"snippet" json:"snippet" binding:"required"`
}
