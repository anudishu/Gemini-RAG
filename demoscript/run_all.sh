#!/bin/bash
# Run all demo steps sequentially

cd "$(dirname "$0")/.." || exit 1

echo "Running all demo steps..."
echo ""

python demoscript/step1_setup.py && \
python demoscript/step2_init_client.py && \
python demoscript/step3_manage_store.py && \
python demoscript/step4_upload_files.py && \
python demoscript/step5_query_store.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ All steps completed successfully!"
else
    echo ""
    echo "❌ One or more steps failed. Please check the output above."
    exit 1
fi
