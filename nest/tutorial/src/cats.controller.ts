import { Controller, Get, Post, Query, Req } from "@nestjs/common";
import { Request } from 'express'

const DEFAULT_ERROR_MESSAGE = '<p>Error fetching your cat :(</p>'

@Controller('cats')
export class CatsController {
	@Post()
	mockCreateCat(): string {
		return 'Cat added'
	}

	@Get()
	async getCatImage(): Promise<string> {
		const response = await fetch('https://api.thecatapi.com/v1/images/search')
		if (!response.ok) return DEFAULT_ERROR_MESSAGE
		const [cat] = await response.json()
		return `<img src="${cat.url}"/>`
	}

	@Get('count')
	async getManyImages(@Req() request: Request): Promise<string> {
		if (!request.query.limit) return "<p>limit query parameter is required</p>"
		const limit = Number(request.query.limit)
		if (!Number.isInteger(limit)) return "<p>limit is not an integer</p>"
		let queryTimes = 1;
		if (limit > 10) queryTimes += limit % 10;
		const promises = []
		for (let i = 0; i < queryTimes; i++) {
			const response = await fetch(
				`https://api.thecatapi.com/v1/images/search?limit=10`
			)
			promises.push(response)
		}
		const responses = await Promise.all(promises)
		const catImages: string[] = []
		for (const response of responses) {
			if (!response.ok) return DEFAULT_ERROR_MESSAGE
			const cats: any[] = await response.json()
			catImages.push(...cats.map(cat => `<img src="${cat.url}"/>`))
		}
		return catImages.filter((_, idx) => {
			return idx < limit
		}).join("<br>")
	}
}
