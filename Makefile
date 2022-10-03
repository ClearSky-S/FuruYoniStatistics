.PHONY: help
## help: prints this help message
help:
	@echo "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':'

.PHONY: update-cdn
## update-cdn: updates the CDN hash
update-cdn:
	@echo Updating CDN hash
	./scripts/update-cdn.sh
