# crdgen/Makefile
# -------------------------------------------------------------

# Pin the kcm revision (override: KCM_REF=v0.2.0 make)
KCM_REF ?= main

# Repo roots/paths
ROOT     := $(shell git rev-parse --show-toplevel)
OUT_FILE := $(ROOT)/docs/reference/crds/index.md
CRD_PATH := templates/provider/kcm/templates/crds

# crdoc binary (auto-install)
CRDOC := $(shell go env GOPATH)/bin/crdoc

.PHONY: api-docs
api-docs: $(CRDOC)
	@TMP_DIR=$$(mktemp -d); \
	echo "Fetching CRDs for $(KCM_REF)…"; \
	git clone --depth 1 --filter=blob:none --sparse \
	  --branch $(KCM_REF) https://github.com/K0rdent/kcm $$TMP_DIR/kcm; \
	git -C $$TMP_DIR/kcm sparse-checkout init --cone; \
	git -C $$TMP_DIR/kcm sparse-checkout set $(CRD_PATH); \
	mkdir -p $$(dirname $(OUT_FILE)); \
	$(CRDOC) --resources $$TMP_DIR/kcm/$(CRD_PATH) --output $(OUT_FILE); \
	rm -rf $$TMP_DIR; \
	echo "Wrote $(OUT_FILE)"

$(CRDOC):
	go install fybrik.io/crdoc@latest

