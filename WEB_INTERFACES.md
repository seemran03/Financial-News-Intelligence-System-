# 🌐 Web Interfaces Guide

This project includes two modern web interfaces for interacting with the Financial News Intelligence System.

## 🎨 Streamlit Interface

### Features
- **Multi-page navigation** with sidebar
- **Rich visualizations** with metrics and tables
- **Real-time processing** with progress indicators
- **Interactive query examples**
- **Database browsing** with search and filters

### Launch
```bash
streamlit run streamlit_app.py
```

The interface will open at `http://localhost:8501`

### Pages

#### 📥 Process News
- **Manual Input**: Enter single article with form
- **JSON Upload**: Upload a JSON file with multiple articles
- **Batch Input**: Paste JSON directly into text area

#### 🔍 Query News
- Natural language query input
- Adjustable max results slider
- Clickable example queries
- Detailed results with entity breakdown

#### 📊 View Database
- Browse all processed articles
- Search by headline
- Sort by date or headline
- View entity information

#### ℹ️ About
- System documentation
- Feature overview
- Technical stack information

---

## 🎨 Gradio Interface

### Features
- **Tabbed interface** for organized workflow
- **Clean, modern design** with Soft theme
- **Interactive components** with real-time updates
- **Data tables** for structured viewing
- **JSON export** capabilities

### Launch
```bash
python gradio_app.py
```

The interface will open at `http://localhost:7860`

### Tabs

#### 📥 Process News
- **Single Article**: Form-based input with headline, content, source, date
- **Batch JSON**: Paste JSON array of articles for bulk processing
- Real-time processing feedback
- JSON output for programmatic use

#### 🔍 Query News
- Natural language query input
- Max results slider
- Results display with markdown formatting
- Entity breakdown section
- Results table (DataFrame)
- JSON export
- Example query buttons

#### 📊 View Database
- Slider to control number of articles
- Database status display
- Articles table with key information
- Sortable columns

#### ℹ️ About
- Complete system documentation
- Feature list
- Architecture overview
- Usage tips

---

## 🚀 Quick Comparison

| Feature | Streamlit | Gradio |
|---------|-----------|--------|
| **Design** | Multi-page dashboard | Tabbed interface |
| **Best For** | Data exploration, analytics | Quick interactions, demos |
| **Customization** | High (CSS, components) | Medium (themes, layouts) |
| **Deployment** | Streamlit Cloud | Hugging Face Spaces, self-hosted |
| **Learning Curve** | Medium | Low |
| **Performance** | Good for dashboards | Fast for simple apps |

## 💡 Usage Tips

### For Processing News
1. Start with a few sample articles to test
2. Use JSON format for batch processing
3. Check the processing results for entity extraction accuracy
4. Review stock impact mappings

### For Querying
1. Use specific company names for direct matches
2. Use sector names for broader results
3. Combine entities for complex queries (e.g., "Banking impact of RBI rate hike")
4. Adjust max results based on your needs

### For Database Viewing
1. Use search to filter articles
2. Sort by date to see latest news first
3. Check entity information to understand extraction quality

## 🔧 Customization

### Streamlit
- Modify `streamlit_app.py` to add custom pages
- Use `st.columns()` for custom layouts
- Add custom CSS in the `st.markdown()` section

### Gradio
- Modify `gradio_app.py` to add new tabs
- Change theme: `gr.themes.Soft()` → `gr.themes.Default()` or custom
- Adjust component sizes with `scale` parameter

## 🐛 Troubleshooting

### Port Already in Use
- **Streamlit**: Change port with `streamlit run streamlit_app.py --server.port 8502`
- **Gradio**: Change port in `app.launch(server_port=7861)`

### System Not Initializing
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify spaCy model: `python -m spacy download en_core_web_sm`
- Check database directory permissions

### No Results in Query
- Process some news articles first
- Check if articles are stored in database
- Verify query syntax and entities

---

**Enjoy using the web interfaces! 🎉**


